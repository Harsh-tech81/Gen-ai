
import OpenAI from "openai";
import dotenv from "dotenv";

dotenv.config();

const client = new OpenAI({
    baseURL: "https://openrouter.ai/api/v1",
    apiKey: process.env.OPENROUTER_API_KEY
});

async function main() {
    try {
        const response = await client.chat.completions.create({
            model: "openai/gpt-4o-mini",
            messages: [
                {
                    role: "user",
                    content: "What is the capital of France?"
                }
            ]
        });

        console.log(response.choices[0].message.content);

    } catch (error) {
        console.error("OpenRouter API Error:", error.message);
    }
}

main();
