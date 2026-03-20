import pickle
import pandas as pd
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Annotated, Literal

with open("model_pickel_titanic_rf", "rb") as f:
    model = pickle.load(f)

app = FastAPI(title="Titanic Survival Predictor 🚢")


# Passenger
class Passenger(BaseModel):
    Pclass: Annotated[
        Literal["First", "Second", "Third"], Field(..., description="Passenger class")
    ]
    Sex: Annotated[Literal["male", "female"], Field(..., description="Gender")]
    Age: Annotated[
        float,
        Field(
            ...,
            gt=0,
            lt=100,
            description="Passenger age in years (child=1-12, adult=18-60)",
        ),
    ]
    SibSp: Annotated[
        int,
        Field(
            ...,
            ge=0,
            le=8,
            description="Siblings/Spouses aboard (0=alone, 1=with partner or sibling, 2+=family group)",
        ),
    ]
    Parch: Annotated[
        int,
        Field(
            ...,
            ge=0,
            le=6,
            description="Parents/Children aboard (0=none, 1=one parent or child, 2+=multiple)",
        ),
    ]
    Fare: Annotated[
        float,
        Field(
            ...,
            gt=0,
            description="Ticket fare in £ (3rd class ~7, 2nd class ~13, 1st class ~75+)",
        ),
    ]
    Embarked: Annotated[
        Literal["C", "Q", "S"],
        Field(..., description="Port (C=Cherbourg, Q=Queenstown, S=Southampton)"),
    ]


@app.get("/")
def home():
    return {"message": "Titanic Survival API is running! 🚢"}


# Predict endpoint
@app.post("/predict")
def predict(passenger: Passenger):

    # Encode inputs
    pclass_encoded = {"First": 1, "Second": 2, "Third": 3}[passenger.Pclass]
    sex_encoded = 0 if passenger.Sex == "male" else 1
    C = 1 if passenger.Embarked == "C" else 0
    Q = 1 if passenger.Embarked == "Q" else 0
    S = 1 if passenger.Embarked == "S" else 0

    data = pd.DataFrame(
        [
            [
                pclass_encoded,
                sex_encoded,
                passenger.Age,
                passenger.SibSp,
                passenger.Parch,
                passenger.Fare,
                C,
                Q,
                S,
            ]
        ],
        columns=["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "C", "Q", "S"],
    )

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    if probability >= 0.7:
        confidence = "High"
    elif probability >= 0.4:
        confidence = "Medium"
    else:
        confidence = "Low"

    return {
        "survived": int(prediction),
        "result": "Survived 👌" if prediction == 1 else "Did Not Survive 😢",
        "survival_probability": round(float(probability), 3),
        "confidence": confidence,
        "input_summary": {
            "class": passenger.Pclass,
            "sex": passenger.Sex,
            "age": passenger.Age,
            "embarked": passenger.Embarked,
        },
    }
