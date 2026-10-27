import {OpenAI} from "openai";
import dotenv from 'dotenv';

dotenv.config();

const client=new OpenAI({
    apikey: process.env.OPENAI_API_KEY
})


client.chat.completions.create({
    model:'gpt-6-luna',
    messages: [
        {
            role: "user",
            content: "What is the capital of France?"
        }
    ]
}).then((response)=>{
    console.log(response.choices[0].message.content);
}).catch((error)=>{
    console.error(error);
});

