import {NextApiRequest, NextApiResponse} from 'next';

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method === 'POST') {
    const {message} = req.body;
    console.log('Received message:', message); // Replace with actual handling
    res.status(200).send('Message received');
  } else {
    res.status(405).send('Method not allowed');
  }
}
