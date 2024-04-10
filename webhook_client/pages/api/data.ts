import createClient from "../../lib/mongodb";

export default async function handler(req: any, res: any) {
  const client = await createClient();
  const db = client.db("test_database");
  const collection = db.collection("stax");

  const data = await collection.find({}).toArray();

  res.json(data);
}
