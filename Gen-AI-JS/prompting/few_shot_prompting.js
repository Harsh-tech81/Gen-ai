
import OpenAI from "openai";
import dotenv from "dotenv";

dotenv.config({ path: "../.env" });

const client = new OpenAI({
    baseURL: "https://openrouter.ai/api/v1",
    apiKey: process.env.OPENROUTER_API_KEY
});

async function main() {
    try {
        const response = await client.chat.completions.create({
            model: "gpt-4o-mini",
            messages: [
                {
                    role: "user",
                    content: `tell me what is 2+3??
                    Example 1:
                    Q: What is 1+1?
                    A: 2
                    Example 2:
                    Q: What is 2+2?
                    A: 4
                    Example 3:
                    Q: What is 3+3?
                    A: 6
                    Give me only answer(A) in your response.
                    
                    `
                }
            ]
        });

        console.log(response.choices[0].message.content);

    } catch (error) {
        console.error("OpenRouter API Error:", error.message);
    }
}

main();
