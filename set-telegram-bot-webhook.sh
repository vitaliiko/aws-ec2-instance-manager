#!/usr/bin/env bash

token=$(cat instance-manager-properties.env | grep TELEGRAM_BOT_TOKEN | awk -F= '{print $2}')
endpoint=$(cat instance-manager-properties.env | grep ENDPOINT | awk -F= '{print $2}')

telegram_api="https://api.telegram.org/bot${token}"
set_webhook_url="${telegram_api}/setWebhook?url=${endpoint}"
check_webhook_url="${telegram_api}/getWebhookInfo"

echo "Set webhook URL: $endpoint"

echo ''
curl $set_webhook_url

echo ''
curl $check_webhook_url

echo ''
