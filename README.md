markdown# W4 - Real Estate Voice Agent | Web3Geeks Capstone Project

### 1. Project Overview
This is the final capstone project of the Web3Geeks Internship. The goal of this project is to build an intelligent AI Voice Agent for the Real Estate industry. In traditional real estate, customers have to manually search portals and call agents. This project automates that process with a conversational voice AI that can understand user needs and provide property information instantly.

This project is maintained as part of a Monorepo which contains all internship daily tasks (Day 2, Day 3... to Capstone).

### 2. Problem Statement
- Manual property searching is time-consuming.
- Real estate agents are not available 24/7.
- No instant voice-based support for property inquiries.
- Lack of automation in scheduling property visits.

### 3. Proposed Solution
An AI-powered Voice Agent that:
- Listens to the user's voice query (e.g., "I need a 3BHK in Faisalabad under 2 crore").
- Processes the intent using AI/NLP.
- Searches from the property database.
- Responds back in natural voice and text.
- Can schedule a site visit for the interested customer.

### 4. Key Features
- **Conversational AI:** Natural language understanding for real estate queries.
- **Smart Search:** Filter properties by Location, Price, Bedrooms, and Type.
- **24/7 Availability:** Acts as a virtual agent that never sleeps.
- **API Based Architecture:** Built with FastAPI for high performance.
- **Health Monitoring:** A `/health` endpoint for uptime checking.
- **Production Ready:** Fully dockerized and integrated with CI/CD pipeline.

### 5. System Architecture
User Voice -> Speech-to-Text -> Intent Understanding (LLM) -> Property Search Logic -> Text-to-Speech -> Voice Response

The backend is a FastAPI server that exposes endpoints. The entire application is containerized using Docker and automatically tested and built using GitHub Actions.

### 6. Tech Stack
- **Backend Framework:** FastAPI (Python)
- **AI & Voice:** OpenAI API / Speech Recognition
- **DevOps:** Docker, GitHub Actions for CI/CD
- **Language:** Python 3.10+

### 7. CI/CD Pipeline Explanation
To ensure code quality and deployment readiness, a CI/CD pipeline is configured at the root `.github/workflows/main.yml`:

1.  **Checkout & Setup:** Workflow checks out the Monorepo and sets up Python.
2.  **Install Dependencies:** Installs requirements from `W4_Real_estate_agent_project/requirements.txt` using `working-directory`.
3.  **Build Docker Image:** Builds Docker image to verify that the Dockerfile is error-free.
4.  **Test Endpoint:** Runs the container and tests the `/health` endpoint. If it returns 200, the pipeline passes (Green Tick).

### 8. How to Run
```bash
cd W4_Real_estate_agent_project
pip install -r requirements.txt
uvicorn main:app --reload9. Future Improvements
Integration with real-time MLS (Multiple Listing Service) API.WhatsApp Voice Bot Integration.Multilingual Support (Urdu + English).Admin Dashboard for Agents to manage leads.
