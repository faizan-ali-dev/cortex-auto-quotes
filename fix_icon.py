import re

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    old_icon = '<i aria-hidden="true" class="icon icon-car"></i>'
    new_icon = '<svg aria-hidden="true" class="e-font-icon-svg e-fas-car" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M499.99 176h-59.87l-16.64-41.6C406.38 91.63 365.57 64 319.62 64H192.38c-45.95 0-86.76 27.63-103.85 70.4L71.88 176H12.01C4.2 176-1.53 183.34.37 190.91l6 24C7.7 220.25 12.5 224 18.01 224h20.07C24.65 235.73 16 252.78 16 272v48c0 16.12 6.16 30.67 16 41.93V416c0 17.67 14.33 32 32 32h32c17.67 0 32-14.33 32-32v-32h256v32c0 17.67 14.33 32 32 32h32c17.67 0 32-14.33 32-32v-54.07c9.84-11.25 16-25.8 16-41.93v-48c0-19.22-8.65-36.27-22.07-48H494c5.51 0 10.31-3.75 11.64-9.09l6-24c1.89-7.57-3.84-14.91-11.65-14.91zM128 352c-17.67 0-32-14.33-32-32s14.33-32 32-32 32 14.33 32 32-14.33 32-32 32zm256 0c-17.67 0-32-14.33-32-32s14.33-32 32-32 32 14.33 32 32-14.33 32-32 32zm-68.65-165.26c-3.13 6.26-9.52 10.27-16.54 10.27h-180.7c-7.03 0-13.41-4.01-16.54-10.27L82.11 148.06c4.54-11.36 15.34-18.91 27.5-18.91h284.77c12.16 0 22.96 7.55 27.5 18.91l-19.47 38.68z"></path></svg>'

    if old_icon in html:
        html = html.replace(old_icon, new_icon)
        print("Replaced missing icon with inline SVG.")
    else:
        print("Icon tag not found!")

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    main()
