# fcc-solutions
My daily solutions to FreeCodeCamp coding challenges, implemented in **Python**. Each file represents a daily challenge!

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 About This Repository

This repo tracks my **coding practice** through FreeCodeCamp challenges, solved in Python. Each file is named by date and includes:

- **Problem description** (as comments at the top)
- **Python solution** with clear function names
- **Test cases** to verify correctness
- **Learning notes** mostly explain more about question at hand


## 📁 Repository Structure

```
daily-python-challenges/
├── README.md
├── 2025/
│   ├── Sep_3_2025_[pangram].py          # Pangram checker
│   ├── Sep_5_2025_[IPv4_Validator].py   # IPv4 address validation
│   ├── Sep_7_2025_[Roman_Numeral_Parser].py  # Roman numeral conversion
│   ├── Sep_8_2025_[Acronym_maker].py    # Acronym generation
│   ├── Sep_12_2025.py                   # Daily challenge
│   ├── Sep_13_2025.py                   # Daily challenge  
│   └── Sep_19_2025.py                   # Daily challenge
└── progress.md                          # Challenge tracker
```

###The Challenges may not be solved in order!

*Total challenges completed: 7 | 

## 💻 Example Solutions

### Sep 5, 2025 - IPv4 Address Validator
**File**: `Sep_5_2025_[IPv4_Validator].py`

```python
"""
IPv4 Validator Challenge
A valid IPv4 address consists of four integers (0-255) separated by dots,
with no leading zeros except for the number 0 itself.
"""

def is_valid_ipv4(ipv4):
    new_ipv4 = ipv4.split(".")
    valid = []
    if len(new_ipv4) == 4:
        for number in new_ipv4:
            if number.isdigit() and 0 <= int(number) <= 255:
                    if len(number) > 1 and number.startswith('0'):
                        valid.append(False)
                    else:
                        valid.append(True)
            else:
                valid.append(False)
    else: 
        return False
    if False in valid:
        return False
    else:
        return True

# Test suite:
print(f"{is_valid_ipv4("192.168.0.30")}") #should return True.
print(f"{is_valid_ipv4("192.168.1.1")}") #should return True.
print(f"{is_valid_ipv4("0.0.0.0")}") #should return True.
print(f"{is_valid_ipv4("255.01.50.111")}") #should return False.
print(f"{is_valid_ipv4("255.00.50.111")}") #should return False.
print(f"{is_valid_ipv4("256.101.50.115")}") #should return False.
print(f"{is_valid_ipv4("192.168.101.")}") #should return False.
print(f"{is_valid_ipv4("192168145213")}") #should return False.
```

## 🛠️ Quick Start

1. **Clone the repo**:
   ```bash
   git clone https://github.com/hassaanabdullah1/fcc-solutions.git
   cd daily-python-challenges
   ```

2. **Run a challenge**:
   ```bash
   python 2025/Sep_5_2025_[IPv4_Validator].py
   ```

3. **Requirements**: Python 3.8+ (no external packages needed)


## 🤝 Contributing & Collaboration

- **Suggestions**: Open an issue with challenge ideas or improvements
- **Alternative Solutions**: Fork and add your approach!
- **Code Reviews**: I'd love feedback on my implementations
- **Challenge Partners**: Let's tackle tough problems together

## 📄 License

MIT License - feel free to use, modify, and share these solutions.

---

*Made with Python 🐍  *
