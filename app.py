from fastapi import FastAPI

app = FastAPI(
    title="Enterprise AI Agent Platform",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "project": "Enterprise AI Agent Platform",
        "developer": "Manvitha Ankam",
        "version": "1.0.0",
        "status": "Running Successfully 🚀"
    }


@app.get("/about")
def about():
    return {
        "developer":"Manvitha"
    }

@app.get("/status")
def status():
    return {
        "status":"Running"
    }

@app.get("/agents")
def agents():
    return {
        "agents":[
            "Planner",
            "Research",
            "Document",
            "Reporter"
        ]
    }

@app.get("/contact")
def contact():
    return {
        "email":"ae22b107@smail.iitm.ac.in"
    }


@app.get("/github")
def github():
    return {
        "github":"https://github.com/Manvitha975"
    }

@app.get('/linkedin')
def linkedin():
    return {
        "linkedin":"https://www.linkedin.com/in/manvitha-ankam/"
    }

@app.get('/resume')
def resume():
    return {
        "resume":"https://drive.google.com/drive/folders/1ok8xt89xEyU4J3dZfF1qSpxDEYaLxWNA"
    }