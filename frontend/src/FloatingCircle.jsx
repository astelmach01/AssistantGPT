import React, { Component } from 'react';
import './FloatingCircle.css';

const colors = ['#00ffff', '#007fff', '#7f00ff'];

class FloatingCircle extends Component {
  constructor(props) {
    super(props);
    this.state = {
      color: colors[Math.floor(Math.random() * colors.length)],
    };
    this.timer = setInterval(() => {
      this.changeColor();
    }, 1000);
  }

  handleMouseEnter = () => {
    clearInterval(this.timer);
  };

  handleMouseLeave = () => {
    this.timer = setInterval(() => {
      this.changeColor();
    }, 1000);
  };

  changeColor = () => {
    // pick a new color that is not already the current color
    let newColor = colors[Math.floor(Math.random() * colors.length)];
    const { color } = this.state;
    while (newColor === color) {
      newColor = colors[Math.floor(Math.random() * colors.length)];
    }
    this.nextColor = newColor;
    this.setState({
      color: this.nextColor,
    });
  };

  render() {
    const { color } = this.state;
    return (
      <div
        className="circle"
        style={{
          border: `5px solid ${color}`,
          borderRadius: '50%',
          boxShadow: `0 0 10px ${color}`,
        }}
        onMouseMove={this.handleMouseEnter}
        onMouseLeave={this.handleMouseLeave}
      />
    );
  }
}

export default FloatingCircle;
