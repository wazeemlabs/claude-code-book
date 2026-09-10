import { chromium } from 'playwright-core';
import fs from 'fs';
const boards = {
  Header:[970,600,'01-header-970x600'], Overlay:[970,300,'spare/03-overlay-970x300'],
  TileStart:[220,220,'02a-tile-start-220x220'], TileBuild:[220,220,'02b-tile-build-220x220'],
  TileAutomate:[220,220,'02c-tile-automate-220x220'], TileScale:[220,220,'02d-tile-scale-220x220'],
  Cards:[300,400,'03-sidebar-cards-300x400'], CoverClaude:[150,300,'spare/05a-cover-claude-code-150x300'],
  CoverLLM:[150,300,'spare/05b-cover-llm-150x300'],
};
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
for (const [name,[w,h,out]] of Object.entries(boards)) {
  const html = fs.readFileSync(`src/${name}.dc.html`,'utf8').replace('<script src="./support.js"></script>','');
  const page = await browser.newPage({ viewport:{width:w,height:h}, deviceScaleFactor:1 });
  await page.setContent(html); await page.waitForTimeout(150);
  await page.screenshot({ path:`png/${out}.png`, clip:{x:0,y:0,width:w,height:h} });
  await page.close(); console.log(out);
}
await browser.close();
