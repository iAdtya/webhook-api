import { MongoClient } from "mongodb";

// i know i am not using .env cz its shared resource
const uri =
  "mongodb+srv://adityakhedekar98906:K6m89IUHPUTnV5Xh@stax-db.phjk2qm.mongodb.net/?retryWrites=true&w=majority";

let client: any;

export async function createClient() {
  if (!client) {
    client = new MongoClient(uri);
    await client.connect();
  }
  return client;
}

export default createClient;
