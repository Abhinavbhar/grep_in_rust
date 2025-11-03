# Rust Grep

This project is a Rust implementation of grep, created as an exercise from [The Rust Programming Language Book](https://doc.rust-lang.org/book/).

It focuses on understanding memory management, file I/O, and performance optimization in Rust.

## Overview

The purpose of this project is to:

- Learn how to efficiently read and process large files in Rust.
- Experiment with different buffer sizes and observe their impact on performance.
- Explore how memory usage and data handling affect search speed.

## How to Run

### 1. Generate a test file

A Python script is included to generate a sample text file. Uncomment the size of text file you want to create.

The script will create a file with the word `rust` appearing 3 times randomly in the text.

### 2. Run the program

```bash
cargo run hello.txt rust
```

This will search for the word "rust" in `hello.txt` file.

### 3. Compare with grep

Try comparing the performance with the standard `grep` command and experiment with different buffer sizes.

## To Do

- [ ] Compare binary instead of string for faster comparison
- [ ] Implement bucket algorithm to make it error proof
- [ ] Improve the searching algorithm
  - One idea: First try to find words of the same size, then match the actual words
- [ ] Implement using multiple threads (only if it provides meaningful performance benefits - don't do it just for the sake of doing it)

## Contributing

feel free to contribute
