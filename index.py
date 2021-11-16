from fastapi import FastAPI

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import tinify
tinify.key = "QWbvxsPzWlwqPP3MHJb6NSlZwKtGWx9d"

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/resize")
def read_item(url, shape):
    print(url, shape)
    source = tinify.from_url(url)
    print(source)

    if shape == '0':
        resized = source.resize(
            method="thumb",
            width=178,
            height=46
        )
    else:
        resized = source.resize(
            method="thumb",
            width=40,
            height=42
        )
    url = resized.store(
        service="s3",
        aws_access_key_id="AKIASIEVADAQ7NTPKH6J",
        aws_secret_access_key="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",
        region="us-west-1",
        path="winesource-website/optimized.png"
        )
    return url