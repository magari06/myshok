const fs = require('fs');
const path = require('path');

const modelsDir = path.resolve(__dirname, 'models');
if (!fs.existsSync(modelsDir)) {
  fs.mkdirSync(modelsDir);
}

const models = ['fox', 'ghost', 'harrenhal'];

models.forEach((name) => {
  const glbPath = path.resolve(__dirname, `${name}.glb`);
  if (!fs.existsSync(glbPath)) {
    console.warn(`File not found: ${glbPath}`);
    return;
  }
  console.log(`Processing ${name}.glb...`);
  const buf = fs.readFileSync(glbPath);
  const b64 = buf.toString('base64');
  const jsContent = `window.__MODEL_DATA_${name} = "${b64}";\n`;
  const outPath = path.resolve(modelsDir, `${name}_model.js`);
  fs.writeFileSync(outPath, jsContent, 'utf8');
  console.log(`Created ${outPath} (${(fs.statSync(outPath).size / 1024 / 1024).toFixed(2)} MB)`);
});
