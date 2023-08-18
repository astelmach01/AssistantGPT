import React, { useState } from 'react';
import axios from 'axios';
import './App.css';
import { Analytics } from '@vercel/analytics/react';
import FloatingCircle from './FloatingCircle';

function App() {
  const [message, setMessage] = useState('');
  const sendMessage = async (text) => {
    try {
      await axios.post('/chat', { message: text });
      console.log('Message sent:', text);
    } catch (error) {
      console.error('Error sending message:', error);
    }
  };
  const handleKeyDown = async (e) => {
    if (e.keyCode === 13) {
      e.preventDefault();
      if (message.trim() !== '') {
        await sendMessage(message);
        setMessage('');
      }
    }
  };

  return (
    <div className="App">
      <Analytics />
      <header className="App-header">
        <h1>Cosmo Chat</h1>
      </header>
      <FloatingCircle />
      <main className="App-main">
        <div className="message-box">
          <textarea
            rows={4}
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Type your message here..."
          />
        </div>
      </main>
    </div>
  );
}

export default App;
