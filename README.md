![MIT License](https://img.shields.io/github/license/efetunca/finger-counter?style=flat-square)

# Finger Counter

A simple project for counting the fingers that appears on the computer's webcam.

The program is able to detect whether the hand is left or right, but it is not yet able to detect both hands at the same time.

## How to Install and Run?

- Clone the project to your computer:

```bash
  git clone https://github.com/efetunca/Finger-Counter.git
```

or simply download the project as ZIP file.

- Go to project directory:

```bash
  cd Finger-Counter
```

- Install necessary modules:

```bash
  sudo pip3 install -r requirements.txt
```

- Run the program:

```bash
  python3 FingerCounter.py
```
  
## Screenshots

![Screenshot 1 - Right Hand with 5 Fingers](https://raw.githubusercontent.com/efetunca/Finger-Counter/main/.github/images/Screenshot_1.jpg)

![Screenshot 2 - Left Hand with No Fingers](https://raw.githubusercontent.com/efetunca/Finger-Counter/main/.github/images/Screenshot_2.jpg)

![Screenshot 3 - Right Hand with 3 Fingers](https://raw.githubusercontent.com/efetunca/Finger-Counter/main/.github/images/Screenshot_3.jpg)

## Future Updates

- The ability to detect both hands at the same will be added.

- The feature of detecting hand signs (e.g. Thumbs Up) will be added.

- Hand detection will be done with a self-written machine learning algorithm instead of the Mediapipe module.

## Related Project

To check out my other project that is similar to this one:

[Virtual Painter](https://github.com/efetunca/Virtual-Painter)
