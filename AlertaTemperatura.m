% Configuración del canal
channelID = TU_CHANNEL_ID; % Reemplaza con tu ID de canal
fieldID = 1; % Número del campo donde guardas la temperatura
readAPIKey = 'TU_READ_API_KEY'; % (opcional) si tu canal es privado

% Leer los últimos datos de temperatura
data = thingSpeakRead(channelID, 'Fields', fieldID, 'NumPoints', 1, 'ReadKey', readAPIKey);

% Verificar si la temperatura supera los 35°C
if data > 35
    fprintf('⚠️ ALERTA: Temperatura alta (%.2f °C) ⚠️\n', data);
else
    fprintf('Temperatura normal: %.2f °C\n', data);
end
