# LinkDecoder 🔍

LinkDecoder is a simple Python tool that helps you **decode suspicious links** which often hide their real destination using hex encoding.

## ✨ Features
- Extracts the `s` parameter from suspicious URLs
- Converts hex strings into readable text
- Reveals the actual destination link

## 🚀 Usage
Run the script in your terminal:

```bash
python decoder.py
```
## example:

```bash
https://getdat.click/?h=xyz123&s=687474703a2f2f6578616d706c652e636f6d2f73656375726974792f74657374
```
### the result:

```bash
http://example.com/security/test
```

