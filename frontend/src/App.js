import React, { Component } from 'react';
import './App.css';
import Nameform from './components/form';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1>SUMMARIZE MY PROFESSOR</h1>
          <Nameform />
           
        </header>
      </div>
    );
  }
}

export default App;
