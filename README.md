# COCOMO Estimation Tool

A Python-based COCOMO (Constructive Cost Model) Estimation Tool that calculates software project estimation values based on Lines of Code (LOC).

## Aim

To apply quantitative software estimation techniques and develop a COCOMO Estimation Tool/Calculator.

## Features

The tool calculates estimation values for:

* Basic COCOMO
* Intermediate COCOMO
* Detailed COCOMO

It supports all three COCOMO project modes:

* Organic
* Semi-Detached
* Embedded

## Input

The user provides:

* Lines of Code (LOC)
* Effort Adjustment Factor (EAF) for Intermediate and Detailed COCOMO

## Output

The tool calculates:

* Effort in Person-Months
* Development Time in Months
* Average Staff Required
* Productivity in LOC/Person-Month

## COCOMO Formulas

### Basic COCOMO

Effort:

```text
Effort = a × (KLOC)^b
```

Development Time:

```text
Time = c × (Effort)^d
```

### Intermediate COCOMO

```text
Effort = a × (KLOC)^b × EAF
```

### Average Staff

```text
Staff = Effort / Development Time
```

### Productivity

```text
Productivity = LOC / Effort
```

## Project Modes

| Mode          | Type                                     |
| ------------- | ---------------------------------------- |
| Organic       | Small and relatively simple projects     |
| Semi-Detached | Medium complexity projects               |
| Embedded      | Complex projects with strict constraints |

## Technologies Used

* Python
* Command Line Interface
* COCOMO Estimation Model

## How to Run

Make sure Python is installed.

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/COCOMO-Estimation-Tool.git
```

Open the project folder:

```bash
cd COCOMO-Estimation-Tool
```

Run the program:

```bash
python cocomo.py
```

## Example Input

```text
Enter Lines of Code (LOC): 10000
Enter EAF: 1.0
```

## Author

Neha Tirpude
