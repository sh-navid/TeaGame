import React, { useState, useEffect } from 'react';

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:5000/auth/protected', { // Replace with your Flask server address
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}` // Assuming you store the token in localStorage after login
          }
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        setMessage(data.message);
      } catch (error) {
        setMessage(`Error: ${error.message}`);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="App">
      <h1>{message}</h1>
    </div>
  );
}

export default App;
