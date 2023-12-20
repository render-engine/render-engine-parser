# Render Engine `BasePageParser`

The `BasePageParser` is used for making content for Render Engine. Parsers are used to parse the content of a page and convert it to HTML. The parser is specified in the page attributes as `Parser`.

This is meant to be used by Render Enging but can be used as a base dependency for building custom Render Engine Parsers.

## Using Frontmatter

[Frontmatter](https://github.com/eyeseast/python-frontmatter) is used to pull in attributes from a generated page.

Some pages will be looking for information that is provided in the frontmatter. All of the attributes defined can be used in the template (which itself can also be defined in the frontmatter or the class itself.

> **NOTE**
> These attributes **CANNOT** be used in the content itself, but you can use them in the template generation.


## Parsing the Data

The base parser doesn't is a pass-thru parser meaning the content input will be passed through.

```md
---
title: "Spider-Man"
name: "Peter Parker"
superhero: "Spider-Man"
---

<h2>I'm your friendly neighborhood Spiderman</h2>

<p>I was bitten by a radioactive spider and now I fight crime.</p>
```

If you generate the page with the following template

```html
<h1>About {{superhero}}</h1>
<h2>Real Name: {{alias}}</h2>

<div>
{{content}}
</div>
```

it would generate.

```html
<h1>About Spider-Man</h1>
<h2>Alias: Peter Parker</h2>

<div>
<h2>I'm your friendly neighborhood Spiderman</h2>

<p>I was bitten by a radioactive spider and now I fight crime.</p>
</div>
```
