# 🔌 Raspberry Pi Pico W – UART Communication using MicroPython

A simple **UART communication** example for the Raspberry Pi Pico W using MicroPython.  
The Pico listens for serial input and prints messages based on the received character.

---

## 🧰 Requirements
- Raspberry Pi Pico / Pico W  
- MicroPython firmware installed  
- Thonny IDE  
- USB-to-TTL converter or another UART device  

---

## ⚙️ Pin Configuration
| Function | Pico Pin | Description |
|-----------|-----------|-------------|
| UART0 TX | GPIO0 | Transmit Data |
| UART0 RX | GPIO1 | Receive Data |
| GND | GND | Common Ground |

---

## 🚀 How It Works
- Send `'a'` → Pico prints **“data on”**  
- Send `'b'` → Pico prints **“data off”**  
- Communication speed: **115200 bps**  

---

## 🧩 Extensions
- Control an LED or relay when receiving `'a'` or `'b'`.  
- Add CRC or checksum for data validation.  
- Send responses back to PC using `serial.write()`.  
