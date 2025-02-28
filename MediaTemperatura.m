% Configuración del canal
channelID = TU_CHANNEL_ID; % Reemplaza con tu ID de canal
fieldID = 1; % Campo donde está la temperatura
readAPIKey = 'TU_READ_API_KEY'; % (opcional si el canal es privado)

% Leer las últimas 10 mediciones de temperatura
numDatos = 10;
temperaturas = thingSpeakRead(channelID, 'Fields', fieldID, 'NumPoints', numDatos, 'ReadKey', readAPIKey);

% Calcular el promedio de temperatura
if ~isempty(temperaturas)  % Verificar que hay datos
    promedio = mean(temperaturas);
    mensaje = sprintf('📊 Promedio de temperatura (últimos %d datos): %.2f °C', numDatos, promedio);
else
    mensaje = 'No hay suficientes datos para calcular el promedio.';
end

% Mostrar el mensaje en MATLAB Analysis
disp(mensaje);
