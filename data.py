FIREFOX_JS = '''
function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
    var dataTransfer = new DataTransfer();
    var dragStartEvent = new DragEvent(
        'dragstart',
        {bubbles: true, cancelable: true, dataTransfer: dataTransfer}
    );
    sourceNode.dispatchEvent(dragStartEvent);
    var dropEvent = new DragEvent(
        'drop', {bubbles: true, cancelable: true, dataTransfer: dataTransfer}
    );
    destinationNode.dispatchEvent(dropEvent);
    var dragEndEvent = new DragEvent(
        'dragend',
        {bubbles: true, cancelable: true, dataTransfer: dataTransfer}
    );
    sourceNode.dispatchEvent(dragEndEvent);
}
simulateHTML5DragAndDrop(arguments[0], arguments[1]);
'''

class Ingredients:
    INGREDIENTS = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}