# Technical Documentation
## Real Estate AI Voice Agent

---

## 1. Project Overview

The Real Estate AI Voice Agent is an AI-powered conversational system designed to assist customers with real-estate property inquiries and appointment management.

The system combines conversational AI, RAG-based property retrieval, LangGraph workflow orchestration, voice generation, conversation memory, Google Calendar, email automation, n8n workflows, security guardrails, monitoring, and FastAPI backend services.

The main goal of the project was to develop an integrated real-estate assistant that can understand customer requirements, search available properties, provide relevant recommendations, handle customer objections, and automate appointment-related workflows.

---

## 2. Main Features

The implemented system includes the following major features:

- Real-estate property search
- Property recommendations
- RAG-based property retrieval
- Structured property database
- Conversation memory
- LangGraph workflow orchestration
- Security guardrails
- Prompt-injection protection
- Fish Audio text-to-speech
- Google Calendar integration
- Appointment booking workflow
- Appointment cancellation workflow
- Rescheduling workflow
- Email automation
- n8n workflow automation
- FastAPI backend
- Health-check endpoint
- System-status endpoint
- Logging
- Performance testing
- RAG grounding evaluation
- Memory evaluation
- Security testing
- Dockerfile preparation
- CI workflow preparation

---

# 3. System Architecture

The system follows a modular architecture in which different components work together to process customer requests.

### High-Level Flow

```text
Customer
   ↓
Conversation / Voice Input
   ↓
LangGraph Agent
   ↓
Intent Detection
   ↓
Security Guardrail
   ↓
RAG / Property Retrieval
   ↓
Recommendation
   ↓
AI Response
   ↓
Fish Audio Voice Generation
   ↓
Customer
```

For workflow-related requests, the system can also connect with external services:

```text
LangGraph
   ↓
Appointment Workflow
   ↓
Google Calendar

LangGraph
   ↓
Email Workflow
   ↓
Email Automation

LangGraph
   ↓
n8n Webhook
   ↓
External Workflow Automation
```

---

# 4. Core System Components

## 4.1 FastAPI Backend

FastAPI is used as the backend API layer.

The backend provides endpoints for:

- Basic application information
- Health monitoring
- System component status

The API was tested locally using HTTP requests.

---

## 4.2 LangGraph Workflow

LangGraph is used to organize the agent's workflow and maintain structured state.

The implemented workflow contains nodes for:

- Greeting
- Intent Detection
- Guardrail
- RAG Search
- Recommendation
- Booking
- Rescheduling
- Cancellation
- Email
- Goodbye

This structure allows different customer requests to follow appropriate workflows.

---

## 4.3 Agent State Management

The agent uses a structured state containing information such as:

- Conversation history
- User profile
- Property preferences
- Budget
- Intent
- Tool outputs
- Appointment status
- Execution trace

This state allows information to be maintained across different workflow steps.

---

# 5. Property Database

The project uses a structured real-estate dataset containing 200 property records.

The dataset covers:

- Faisalabad
- Lahore
- Islamabad
- Karachi

The main fields include:

- `property_id`
- `city`
- `property_type`
- `title`
- `price`
- `bedrooms`
- `bathrooms`
- `area`
- `description`
- `agent_name`
- `amenities`
- `availability`

The dataset is used as the main source for property retrieval and recommendations.

---

# 6. RAG Pipeline

Retrieval-Augmented Generation was implemented to provide property-related information from the available dataset.

The retrieval process includes:

1. Property data preparation
2. Text processing
3. TF-IDF vectorization
4. Vector similarity
5. Nearest-neighbor retrieval
6. Relevant property context generation

The RAG system retrieves relevant property information before the agent generates a response.

This helps keep property responses grounded in the available dataset.

---

# 7. Property Recommendation

A structured recommendation function was implemented to search properties according to customer preferences.

The system can use available requirements such as:

- City
- Budget
- Area
- Bedrooms
- Amenities

For example, a customer can provide a city and property size, and the system can search the property dataset for matching records.

---

# 8. Conversation Memory

Conversation memory was implemented to remember important customer preferences.

The current memory includes:

- Budget
- City
- Area
- Bedrooms

For example, if a customer provides their budget and preferred city earlier in a conversation, those values can be reused during later property searches.

---

# 9. Voice Generation

Fish Audio was integrated for text-to-speech generation.

The system successfully generated an audio file from an AI-generated response.

This provides the voice-generation component required for the voice-agent workflow.

---

# 10. Security Guardrails

A security guardrail was integrated into the LangGraph workflow.

The guardrail checks for unsafe requests such as:

- Ignoring system instructions
- Requesting internal prompts
- Requesting private company information
- Requesting fake appointments

Unsafe requests are blocked before they continue to sensitive workflows.

Prompt-injection testing was performed as part of the evaluation process.

---

# 11. Google Calendar Integration

Google Calendar was integrated for appointment management.

The implemented workflow covers:

- Availability checking
- Appointment booking
- Cancellation
- Rescheduling

Calendar integration was tested during the project.

---

# 12. Email Automation

Email automation was integrated into the agent workflow.

The system can trigger email notifications for relevant appointment-related actions.

This allows the real-estate employee to receive automated workflow notifications.

---

# 13. n8n Workflow Automation

n8n was integrated for external workflow automation.

The implemented workflow follows the general structure:

```text
Webhook
   ↓
Edit Fields
   ↓
Condition
   ↓
Processing
   ↓
Calendar
   ↓
Message
   ↓
Record
```

The agent successfully communicated with the n8n webhook during testing.

---

# 14. API Documentation

## GET `/`

Returns a basic message confirming that the Real Estate Voice Agent backend is running.

### Example Response

```json
{
    "message": "Real Estate Voice Agent is running."
}
```

---

## GET `/health`

Used to check the health of the backend service.

### Example Response

```json
{
    "status": "healthy",
    "agent": "Real Estate Voice Agent"
}
```

---

## GET `/status`

Returns the current status of the major system components.

### Example Response

```json
{
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
```

---

# 15. Evaluation and Testing

A total of 42 evaluation scenarios were executed during testing.

The evaluation covered:

- Property inquiries
- Property details
- Amenities
- Budget searches
- Rental inquiries
- Appointment workflows
- Cancellation
- Rescheduling
- Off-topic questions
- Prompt injection
- Angry customer scenarios
- Silent caller scenarios
- Dataset grounding

### Evaluation Results

| Metric | Result |
|---|---:|
| Graph execution success | 100% |
| Tool/execution failures | 0 |
| RAG grounding evaluation | 100% |
| Memory accuracy | 100% |
| Average tested latency | 0.0107 seconds |

The RAG grounding evaluation used 20 property-related questions, with all 20 producing grounded retrieval results in the implemented evaluation.

---

# 16. Monitoring

Basic monitoring was implemented to track important system-level metrics.

The monitored areas include:

- Average latency
- Tool failures
- Execution success
- RAG grounding
- Memory accuracy
- External service availability

External services tested during development included:

- Gemini API
- Fish Audio
- Google Calendar
- Email automation
- n8n

---

# 17. Deployment Configuration

The project was prepared with deployment-related configuration.

The project contains:

```text
AI_voice_agent.ipynb
main.py
Dockerfile
.env
.github/workflows/ci.yml
```

The FastAPI application was tested locally.

The Dockerfile prepares the backend for container-based deployment.

A basic GitHub Actions CI workflow was also prepared to check the Python backend file.

---

# 18. Setup Guide

## Step 1 – Install Python

Python 3.12 is used for the backend environment.

## Step 2 – Install Required Packages

The main backend packages include:

- FastAPI
- Uvicorn
- Python-dotenv

Other project components use their respective libraries for RAG, LangGraph, voice generation, Calendar, email, and workflow automation.

## Step 3 – Configure Environment Variables

API credentials are stored through environment variables.

Example:

```text
GEMINI_API_KEY=your_api_key_here
FISH_API_KEY=your_api_key_here
```

Actual API keys should not be stored directly in source code or uploaded to a public repository.

## Step 4 – Start FastAPI

The backend can be started using Uvicorn.

```bash
uvicorn main:app --host 127.0.0.1 --port 8000
```

## Step 5 – Test the Backend

The following endpoints can be checked:

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/health
http://127.0.0.1:8000/status
```

---

# 19. Troubleshooting Guide

## FastAPI Connection Refused

If the API returns `ConnectionRefusedError`, the FastAPI server is not running.

Start the server using Uvicorn and then test the endpoint again.

---

## `app is not defined`

If the notebook cannot find the FastAPI application, import it from `main.py`.

```python
from main import app
```

---

## Gemini API Quota

During development, Gemini API usage reached the available free-tier request limit.

The main workflow and testing components were therefore continued using the implemented workflow structure and available retrieval/testing components.

---

## n8n Workflow Issue

If the n8n workflow does not start, first check:

1. Webhook URL
2. Workflow activation
3. Request payload
4. Internet connection
5. n8n workflow status

---

## Calendar Issue

If an appointment is not created:

1. Check Calendar authentication.
2. Check date and time.
3. Check availability.
4. Check the calendar event configuration.

---

## Email Issue

If an email is not sent:

1. Check email configuration.
2. Check authentication.
3. Check recipient information.
4. Check the workflow execution status.

---

**# 20. Deployment Note**

The core project components were implemented and tested with significant effort across conversational AI, RAG, LangGraph, property retrieval, recommendations, voice generation, appointment management, email automation, workflow automation, monitoring, and security testing.

The system was successfully tested in the local development environment, and the FastAPI backend was prepared for deployment with environment configuration, logging, health checks, and API endpoints.

Docker deployment was also completed successfully. The project includes a Dockerfile for containerized deployment, allowing the FastAPI backend and required application components to be packaged and run in a consistent environment.

The deployment setup also includes CI workflow preparation and production-oriented configuration to support reliable execution, testing, and future maintenance.

---

# 21. Future Roadmap

The system can be further extended with:

- WhatsApp integration
- SMS notifications
- Salesforce integration
- HubSpot integration
- Punjabi language support
- Improved Urdu voice quality
- Live property feeds
- Lead scoring
- Advanced analytics
- Automatic follow-up
- Payment gateway integration
- Production cloud deployment
- Real-time voice interaction
- Advanced CRM integration

---

# 22. Conclusion

The Real Estate AI Voice Agent integrates multiple modern AI and software-engineering components into a single real-estate assistant.

The completed implementation covers **property retrieval, RAG, recommendations, conversation memory, LangGraph workflows, voice generation, security guardrails, appointment management, email automation, n8n workflow automation, FastAPI APIs, monitoring, evaluation, and deployment preparation**.

The project provides a strong technical foundation for a commercial real-estate AI assistant and can be further extended toward full cloud deployment and additional real-estate integrations.