
// Función auxiliar para limpiar el contenedor y evitar duplicados
function clean_graph(element_id) {
    const element = document.getElementById(element_id);
    if (element) {
        element.innerHTML = '';
    }
}

/**
 * Función Maestra para Renderizar Gráficos
 * @param {Array} data - El arreglo de datos (freq_abs, freq_rel, etc.)
 * @param {String} element_id - El ID del div HTML donde se pintará
 * @param {String} graph_type - 'bar' | 'donut' | 'line' | 'area'
 * @param {String} data_type - 'num' (numérico) | 'char' (cualitativo/texto)
 * @param {String} label_text - El texto flotante que saldrá al pasar el mouse
 */
function render_graph(data, element_id, graph_type, data_type, label_text) {
    // 1. Limpiar el contenedor siempre antes de dibujar
    clean_graph(element_id);
    
    if (!data || data.length === 0) return;

    // 2. Si el dato es numérico, ordenarlo para que las líneas y barras no se crucen
    if (data_type === 'num') {
        data.sort((a, b) => parseFloat(a.x) - parseFloat(b.x));
    }

    // 3. Evaluar el tipo de gráfico solicitado mediante los nuevos argumentos
    switch (graph_type) {
        case 'bar':
            new Morris.Bar({
                element: element_id,
                data: data,
                xkey: 'x',
                ykeys: ['y'],
                labels: [label_text],
                barColors: ['#3498db'],
                resize: true
            });
            break;

        case 'donut':
            // Morris.Donut requiere estrictamente propiedades 'label' y 'value'
            const donutData = data.map(item => ({
                label: String(item.x),
                value: parseFloat(item.y)
            }));
            
            new Morris.Donut({
                element: element_id,
                data: donutData,
                colors: ['#2ecc71', '#3498db', '#9b59b6', '#f1c40f', '#e74c3c'],
                resize: true,
                formatter: function (value) { return value + '%'; }
            });
            break;

        case 'line':
            new Morris.Line({
                element: element_id,
                data: data,
                xkey: 'x',
                ykeys: ['y'],
                labels: [label_text],
                lineColors: ['#e67e22'],
                lineWidth: 3,
                parseTime: false,
                resize: true
            });
            break;

        case 'area':
            new Morris.Area({
                element: element_id,
                data: data,
                xkey: 'x',
                ykeys: ['y'],
                labels: [label_text],
                lineColors: ['#9b59b6'],
                fillOpacity: 0.3,
                parseTime: false,
                resize: true
            });
            break;
            
        default:
            console.error("Tipo de gráfico no reconocido: " + graph_type);
    }
}