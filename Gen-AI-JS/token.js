import { get_encoding } from "tiktoken";
const encoderForGPT = get_encoding("gpt2");

const encoded=encoderForGPT.encode("Hello, world!");
console.log(encoded);

const decoded=encoderForGPT.decode(encoded);
console.log(new TextDecoder().decode(decoded));