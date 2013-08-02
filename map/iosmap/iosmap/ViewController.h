//
//  ViewController.h
//  iosmap
//
//  Created by homata on 2013/08/02.
//  Copyright (c) 2013年 homata. All rights reserved.
//

#import <UIKit/UIKit.h>
#import <MapKit/MapKit.h>

@interface ViewController : UIViewController <MKMapViewDelegate, CLLocationManagerDelegate> {
    //IBOutlet MKMapView *mapView;
    //CLLocationManager *locationManager;
}

//@property (nonatomic, retain) CLLocationManager *locationManager;
//@property (strong, nonatomic) IBOutlet MKMapView *mapView;

@end
