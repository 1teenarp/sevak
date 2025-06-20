#!/bin/bash

echo "🔧 Initializing Sevak monorepo..."

# Create directory structure
mkdir -p agent_system/{services/{file_service,vision_service},agent/strategies,shared,data}

cd agent_system

# Create docker-compose.yml

# Create services/vision_service files

# Create agent/agent_core.py

# Create shared utils and ollama client

touch agent/strategies/vision_workflow.py
touch services/file_service/README.md

echo "✅ Sevak monorepo scaffold complete!"
