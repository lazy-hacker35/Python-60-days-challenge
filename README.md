  ## 📌 Problem Statement
Given an array of integers `nums` and an integer `target`, return the **indices of the two numbers** such that their sum is equal to `target`.

Constraints:
- Each input has **exactly one valid solution**
- You may **not use the same element twice**
- The order of the output does not matter

---

## 🧠 Approach
- Use a dictionary (hash map) to store numbers and their indices
- Traverse the array once
- For each element:
  - Calculate the required value as `target - current_number`
  - Check if this value already exists in the hash map
- If it exists, return the indices of the current number and the stored number
- Otherwise, store the current number with its index in the map

This approach avoids nested loops and improves efficiency.

---

## ⏱️ Time & Space Complexity
- **Time Complexity:** O(n)  
  (Each element is processed once)

- **Space Complexity:** O(n)  
  (Extra space used for the hash map)
