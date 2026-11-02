import { GoogleGenAI } from '@google/genai';
import dotenv from "dotenv";

dotenv.config({ path: "../.env" });

const ai = new GoogleGenAI();

async function main() {
  const response = await ai.models.generateContent({
    model: 'gemini-3.8-flash',
    contents: 'Why is the sky blue?',
  });
  console.log(response.text);
}

main();