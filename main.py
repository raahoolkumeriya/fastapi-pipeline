from fastapi import FastAPI

tags_metadata = [
    {
        "name": "Space",
        "description": "Infinity towards Infinity",
        "externalDocs": {
            "description": "website",
            "url": "https://codelocked.herokuapp.com/",
        },
    },
]

app = FastAPI(
    title="Interface",
    description="Development and Delivery at One place",
    version="1.0.0",
    openapi_tags=tags_metadata,
    openapi_url="/api/v1/openapi.json")


@app.get("/", tags=["Space"])
def read_root():
    """
    The universe is all of space and time and their contents, including planets, stars, galaxies,
    and all other forms of matter and energy. The Big Bang theory is the prevailing cosmological 
    description of the development of the universe.

        Shape: Flat with a 0.4% margin of error
    """
    return {"message from universe": "Welcome Aboard to Interface universe!!!"}

