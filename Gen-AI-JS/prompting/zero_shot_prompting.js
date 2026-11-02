
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
            model: "nvidia/nemotron-3-ultra-550b-a55b:free",
            messages: [
                {
                    role: "user",
                    content: "tell me what is 2+3"
                }
            ]
        });

        console.log(response.choices[0].message.content);

    } catch (error) {
        console.error("OpenRouter API Error:", error.message);
    }
}

main();
