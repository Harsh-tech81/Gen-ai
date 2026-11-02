import dotenv from "dotenv";
import OpenAI from 'openai';
// import { z } from 'zod';
// import { zodTextFormat } from 'openai/helpers/zod';

dotenv.config({ path: "../.env" });


const client = new OpenAI();


async function init() {
    const result=await client.responses.create({
        model:'gpt-4.1-mini',
        input:'Hey there, My name is Harsh Kumar'
    });
    console.log(result.output_text);

}

init()
