package main

import (
	"context"
	"fmt"

	"github.com/9bany/ai-explore/internal/llm"
	"github.com/9bany/ai-explore/internal/swarm"
	dotenv "github.com/joho/godotenv"
)

func main() {
	dotenv.Load()

	client := swarm.NewSwarm("", llm.Ollama)

	agent := &swarm.Agent{
		Name:         "Agent",
		Instructions: "You are a helpful agent.",
		Model:        "llama3.1",
	}

	messages := []llm.Message{
		{Role: llm.RoleUser, Content: "What is 42 multiplied by 56?"},
	}

	ctx := context.Background()
	response, err := client.Run(ctx, agent, messages, nil, "", false, false, 5, true)
	if err != nil {
		panic(err)
	}

	fmt.Println(response.Messages[len(response.Messages)-1].Content)
}
