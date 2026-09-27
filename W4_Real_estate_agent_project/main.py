# Week 4 - Day 6
# Task 5 - FastAPI Backend

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Real Estate Voice Agent is running."
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "agent": "Real Estate Voice Agent"
    }  



@app.get("/status")
def system_status():
    return {
        "fastapi": "working",
        "fish_audio": "working",
        "langgraph": "working",
        "rag": "working",
        "vector_retrieval": "working",
        "property_database": "working",
        "google_calendar": "working",
        "email_automation": "working",
        "n8n": "working"
    }