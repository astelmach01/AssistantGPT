'use client'

import {useState, ChangeEvent, KeyboardEvent} from 'react';
import axios from 'axios';

export default function Chat() {
  const [message, setMessage] = useState<string>('');

  const handleKeyDown = async (e: KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      try {
        await axios.post('/api/chat', {message});
        setMessage('');
      } catch (error) {
        console.error('Error sending message:', error);
      }
    }
  };

  const handleInputChange = (e: ChangeEvent<HTMLInputElement>) => {
    setMessage(e.target.value);
  };

  return (
    <div style={{
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      height: '100vh',
      flexDirection: 'column'
    }}>
      <h1 style={{marginBottom: '2rem'}}>Cosmo</h1>
      <input
        type="text"
        placeholder="Type a message and press Enter"
        value={message}
        onChange={handleInputChange}
        onKeyDown={handleKeyDown}
        style={{padding: '0.5rem', width: '300px'}}
      />
    </div>
  );
}
