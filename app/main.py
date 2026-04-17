from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(
    title="Informed Learning Backend",
    description="Minimal backend used to learn Kubernetes with a simple Deployment and Service.",
    version="0.1.0",
)


class AnalyzeRequest(BaseModel):
    text: str


class Assessment(BaseModel):
    rating: str
    reason: str


class AnalyzeResponse(BaseModel):
    assessments: dict[str, Assessment]


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest) -> AnalyzeResponse:
    text = request.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="text must not be empty")

    lowered = text.lower()
    assessments: dict[str, Assessment] = {}

    if "sugar" in lowered:
        assessments["Sugar"] = Assessment(
            rating="unhealthy",
            reason="High added sugar is usually treated as a less healthy ingredient.",
        )

    if "oats" in lowered:
        assessments["Oats"] = Assessment(
            rating="healthy",
            reason="Oats are commonly treated as a fiber-rich whole grain ingredient.",
        )

    if "salt" in lowered:
        assessments["Salt"] = Assessment(
            rating="neutral",
            reason="Salt is not automatically bad, but intake depends on quantity and context.",
        )

    if not assessments:
        assessments["Unknown"] = Assessment(
            rating="neutral",
            reason="This learning app returns mocked assessments for a small sample of ingredients.",
        )

    return AnalyzeResponse(assessments=assessments)
