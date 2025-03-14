# README

## Modified sdhash for Malware Analysis

This tool is based on the original **sdhash**, which can be found at:
[https://github.com/sdhash/sdhash](https://github.com/sdhash/sdhash)

This version has been modified by **Moia et al.**, as published in:
[https://sol.sbc.org.br/index.php/sbseg\_estendido/article/view/19263](https://sol.sbc.org.br/index.php/sbseg_estendido/article/view/19263)

### Purpose

This tool is designed for **malware analysis**, following the methodology described in **Botacin et al.**:
[https://www.sciencedirect.com/science/article/abs/pii/S2666281721001281](https://www.sciencedirect.com/science/article/abs/pii/S2666281721001281)

### Features

- **Modified similarity hashing** for enhanced malware detection.
- Optimized **comparison mechanisms** for binary analysis.
- Compatible with **large datasets** for batch processing.
- Supports integration with **existing forensic tools**.

### Installation

```bash
# Clone the repository
git clone https://github.com/your-repo/sdhash-modified.git
cd sdhash-modified

# Compile the tool
make
```

### Alternative Installation (Precompiled Binary)

```bash
# Download precompiled SDhash

wget $(curl -s https://api.github.com/repos/Botacin-s-Lab/SDHash/releases/latest | grep "browser_download_url" | cut -d '"' -f 4) -O SDhash

# Make SDhash executable
chmod +x SDhash

# Optionally move SDhash to a global bin location (e.g., /usr/local/bin) to run it anywhere
mv SDhash /usr/local/bin/sdhash
```

### Usage

```bash
# HELP
sdhash -h

```

