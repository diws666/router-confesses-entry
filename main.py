import os

# Verified count: 134 characters (1 line, UTF-8, no trailing newline)
LINE = "The Wi-Fi died at the best part of the movie. The router blinked twice and confessed it just wanted us to talk to each other for once."

out_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
with open(os.path.join(out_dir, 'entry.txt'), 'w', encoding='utf-8', newline='') as f:
    f.write(LINE)

print(len(LINE))
