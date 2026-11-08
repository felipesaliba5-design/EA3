# Teste de comunicação HTTP com o Webhook do EduBot via PowerShell
param(
    [string]$WebhookUrl = "https://n8n.incluc0de.com.br/webhook/chat"
)

$Body = @{
    message    = "Qual é a data limite para a entrega do projeto final do Bootcamp Front-End React?"
    session_id = "sessao-edubot-$(Get-Random)"
} | ConvertTo-Json -Compress

$Headers = @{
    "Content-Type" = "application/json"
    "Accept"       = "application/json"
}

Write-Host "[*] Enviando requisição POST para: $WebhookUrl" -ForegroundColor Cyan
Write-Host "[*] Payload: $Body" -ForegroundColor Gray

try {
    $Response = Invoke-RestMethod -Uri $WebhookUrl -Method Post -Headers $Headers -Body $Body -TimeoutSec 60
    Write-Host "[+] Resposta recebida com sucesso:" -ForegroundColor Green
    $Response | ConvertTo-Json -Depth 5
}
catch {
    Write-Host "[-] Falha ao chamar o webhook: $_" -ForegroundColor Red
}
