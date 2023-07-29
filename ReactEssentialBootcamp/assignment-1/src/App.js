import React, { useState } from 'react';
import './App.css';


function App() {
  const [isDarkMode, setIsDarkMode] = useState(false);

  const handleToggle = () => {
    setIsDarkMode((prevIsDarkMode) => !prevIsDarkMode);
  };
  return (
    <div className={`App ${isDarkMode ? 'dark' : ''}`}>
        <h1>Toggle Background Color</h1>
        <button onClick={handleToggle}>Toggle</button>
    </div>
  );
}

export default App;
