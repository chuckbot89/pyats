def count_down_interfaces(parsed_output):
    interfaces = parsed_output['interface']
    
    count = 0
    
    for intf_data in interfaces.values():
        
        status = intf_data['status']
        
        if status == 'down':
            count += 1
    
    return count
