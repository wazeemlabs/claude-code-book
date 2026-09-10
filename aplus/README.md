# Amazon A+ content

- `copy.md`: the text of every module, in page order
- `labels.md`: an image keyword under 100 characters for each image
- `png/`: the six module images at Amazon's exact pixel sizes, ready to upload
- `png/spare/`: the stats strip and comparison chart covers, cut to stay within six images
- `src/`: the artboard sources and canvas layout the images are rendered from
- `render.mjs`: re-renders `png/` from `src/` (`npm i playwright-core`, then `node render.mjs`)

The chapter ranges under the four part tiles are a guess; check them
against the manuscript before upload.
