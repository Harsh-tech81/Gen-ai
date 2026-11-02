
import dotenv from "dotenv";
import OpenAI from "openai";

dotenv.config({ path: "../.env" });

const client = new OpenAI({
    baseURL: "https://openrouter.ai/api/v1",
    apiKey: process.env.OPENROUTER_API_KEY,
});

async function init() {
    try {
        const result = await client.chat.completions.create({
            model: "nvidia/nemotron-3-ultra-550b-a55b:free",
            messages: [
                {
                    role: "user",
                    content: "Hey there, my name is Harsh Kumar."
                }
            ]
        });

        console.log(result.choices[0].message.content);

    } catch (error) {
        console.error("OpenRouter API Error:", error.message);
    }
}

init();
