# sevak
helper

I try to help you with what I can best.
I will learn to better my understanding capabilities later.
I will focus more on doing what I am enabled to do so effectively.


                        [ AGENT LAYER ]
                             ↓
                ┌────────────────────────┐
                │ Agent (Python process) │
                └────────────┬───────────┘
                             ↓
     ┌──────────────────────────────────────────────────────┐
     │             SERVICE LAYER (Dockerized)               │
     │ ┌────────────┐ ┌──────────────┐ ┌───────────────┐    │
     │ │ file_svc   │ │ vision_svc   │ │ db_svc        │    │
     │ │ (REST/gRPC)│ │ (REST/gRPC)  │ │ (PostgreSQL)  │    │
     │ └────────────┘ └──────────────┘ └───────────────┘    │
     └──────────────────────────────────────────────────────┘
                             ↓
               ┌─────────────────────────────┐
               │ Local File System / Ollama  │
               └─────────────────────────────┘

