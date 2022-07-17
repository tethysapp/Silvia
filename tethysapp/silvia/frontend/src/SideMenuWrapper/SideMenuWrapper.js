import React from "react";
import {SideMenu} from '../styles/SideMenu.styled'
import Dropdown from "react-bootstrap/Dropdown";
import DropdownButton from "react-bootstrap/DropdownButton";
import "bootstrap/dist/css/bootstrap.min.css";

const SideMenuWrapper = ({ style, onLayer,layer,dates,actual_date,opacity_wms,wms_op_val}) => {

  const opacityHandler = (data) => {

    opacity_wms(data);
  }

  return(
    
      <SideMenu>
        <div className="wrapper_absolute">
        <p className="sudo_title">
          Landslides Events
        </p>
        <div className="mycontainer">
          
          <p className="prompt">Select Dates</p>
          <DropdownButton 
            id="dropdown-button-dark-example2"
            variant="secondary"
            menuVariant="dark"
            title={actual_date}
            size= 'lg'
            onSelect={(event) => style(event)}
          >
          {dates.map((date, index) => (
            
            <Dropdown.Item  eventKey={date} key={index}>{date}</Dropdown.Item>
          ))}
          </DropdownButton>    
        </div>
        <input
          type="checkbox"
          checked={layer}
          onChange={(event) => onLayer(event)}
          className="input_name"
        /> 
        <span className="span_div">Hide/show</span>
        <div className="mainContainer">
        <p className="sudo_title">
          Landslides Zones
        </p>
        <div className="mycontainer">
          <p className="prompt">Contrast</p>
          <div className="buble span_div"> 
              {wms_op_val}
          </div>
          <div className="slider-parent">
              <input type="range" min="0" max="1"  step="0.1" value={wms_op_val}
                onChange={({ target: { value: radius } }) => {
                            opacityHandler(radius);
                          }}
              />
          </div>
        </div> 

        </div>

        </div>        

      </SideMenu>


  );
};

export default SideMenuWrapper;