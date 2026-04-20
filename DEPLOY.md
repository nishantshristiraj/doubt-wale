# Deploy Doubt Wale

## 1. GitHub
1. Create repo `doubt-wale`
2. Upload entire folder
3. Enable GitHub Pages: Settings > Pages > Source: /website

## 2. Backend on Render
1. Go to render.com > New Web Service > Connect GitHub repo
2. Root: /backend
3. Build: pip install -r requirements.txt
4. Start: uvicorn main:app --host 0.0.0.0 --port $PORT
5. Add env vars: OPENAI_API_KEY

## 3. WhatsApp Sandbox
1. developers.facebook.com > Create App > Business > WhatsApp
2. Add WhatsApp > API Setup > use test number
3. Webhook URL: https://your-render-url/webhook
4. Verify token: doubtwale123
5. Subscribe to messages
6. Test: send "Hi" from your phone to test number
