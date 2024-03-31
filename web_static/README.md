# README: Introduction to HTML and CSS

## HTML
HTML (Hypertext Markup Language) is a markup language used for creating the structure and content of webpages. It provides a set of tags or elements that define the different parts of a webpage, such as headings, paragraphs, images, links, and more.

## Creating an HTML Page
To create an HTML page, follow these steps:
1. Open a text editor.
2. Start with an HTML document declaration: `<!DOCTYPE html>`.
3. Create the `<html>` element as the root of the document.
4. Inside the `<html>` element, include the `<head>` and `<body>` elements.
5. In the `<head>` element, add metadata like the page title, character encoding, and linked stylesheets or scripts.
6. Inside the `<body>` element, add the content and structure of your webpage using various HTML tags.

## Markup Language
A markup language is a system for annotating text to denote its structure and presentation. HTML is an example of a markup language as it uses tags to define the structure and formatting of content within a document.

## DOM (Document Object Model)
The DOM is a programming interface for HTML and XML documents. It represents the structure of a webpage as a tree-like structure, where each element, attribute, and text node becomes a part of the model. The DOM allows scripts to dynamically access and manipulate the content, structure, and style of a webpage.

## Element / Tag
In HTML, an element, also known as a tag, represents a specific type of content or structure within a webpage. Elements are enclosed in angle brackets, such as `<h1>`, `<p>`, or `<img>`. They can have attributes and may contain other elements or text.

## Attribute
Attributes provide additional information about an HTML element. They are specified within the start tag of an element and consist of a name and a value. Attributes can modify the behavior or appearance of an element, such as setting its ID, class, or source URL.

## Loading a Webpage in a Browser
When a browser loads a webpage, it follows these steps:
1. The browser requests the HTML file from the web server.
2. The server sends the HTML file back to the browser.
3. The browser parses the HTML and builds the DOM tree.
4. The browser requests additional resources like CSS files, images, or JavaScript files referenced in the HTML.
5. The browser combines the HTML, CSS, and JavaScript to render and display the webpage.

## CSS (Cascading Style Sheets)
CSS is a stylesheet language used to describe the presentation and style of an HTML document. It allows you to control the layout, colors, fonts, and other visual aspects of a webpage.

## Adding Style to an Element
To add style to an HTML element using CSS, you can:
1. Use inline styles: Apply styles directly within the HTML tag using the `style` attribute.
2. Use internal stylesheets: Define styles within the `<style>` tags in the `<head>` section of the HTML document.
3. Use external stylesheets: Create a separate CSS file and link it to the HTML document using the `<link>` element.

## Class
A class is a way to group elements with similar characteristics or styles. By assigning the same class to multiple elements, you can apply styles or JavaScript behavior to them collectively.

## Selector
Selectors are patterns used to select elements in CSS. They specify which elements should be styled based on their tag name, class, ID, attributes, or relationships with other elements. For example, you can use the tag selector (`h1`), class selector (`.my-class`), or ID selector (`#my-id`) to target specific elements.

## CSS Specificity Value
CSS specificity determines the priority of styles when multiple selectors target the same element. Specificity is calculated based on the selector types and their combinations. Specificity values are assigned to each selector, and the selector with the highest specificity value takes precedence.

## Box Properties in CSS
Box properties in CSS control the layout and dimensions of elements. Some common box properties include:
- `width` and `height`: Set the width and height of an element.
- `margin`: Defines the space around an element.
- `padding`: Defines the space between the content and the element's border.
- `border`: Sets the border properties of an element.
- `box-sizing`: Specifies how the width and height of an element are calculated, including or excluding padding and border.

Feel free to explore and experiment with HTML and CSS to create visually appealing and structured webpages.