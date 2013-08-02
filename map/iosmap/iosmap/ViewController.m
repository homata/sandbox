//
//  ViewController.m
//  iosmap
//
//  Created by homata on 2013/08/02.
//  Copyright (c) 2013年 homata. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController

//@synthesize mapView;
//@synthesize locationManager;

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
    /*
    self.locationManager = [[[CLLocationManager alloc] init]autorelease];
    locationManager.delegate = self;
    [locationManager startUpdatingLocation];//位置情報の取得開始
    mapView.showsUserLocation = YES;
     */
    // 生成
    MKMapView *mv = [[MKMapView alloc] init];
    mv.frame = CGRectMake(0,0,320,480);
    
    // 表示位置を設定
    CLLocationCoordinate2D co;
    // 東京都庁の経度緯度
    //co.latitude = 35.68664111;  // 経度
    //co.longitude = 139.6948839; // 緯度
    // 鯖江駅
    co.latitude  = 35.943187; // 経度
    co.longitude = 136.188701; // 緯度
    [mv setCenterCoordinate:co animated:NO];
    
    // 縮尺を指定
    MKCoordinateRegion cr = mv.region;
    cr.center = co;
    cr.span.latitudeDelta = 0.001; //0.5;
    cr.span.longitudeDelta = 0.001; // 0.5;
    [mv setRegion:cr animated:NO];
    
    // addSubview
    [self.view addSubview:mv];
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

//表示領域の設定
/*
-(void)locationManager:(CLLocationManager *)manager didUpdateToLocation:(CLLocation *)newLocation fromLocation:(CLLocation *)oldLocation{
    MKCoordinateRegion region = mapView.region;
    region.center = newLocation.coordinate;//画面の中心座標を指定する
    region.span.latitudeDelta = 0.01;//南北の距離
    region.span.longitudeDelta = 0.01;//東西の距離
    [mapView setRegion:region];
    [locationManager stopUpdatingLocation];//このメソッド呼び出さないと、連続して情報取得されるので、呼び出して終了しておく
}
*/
/*
-(void)locationManager:(CLLocationManager *)manager didFailWithError:(NSError *)error{
    [locationManager stopUpdatingLocation];
}
*/
/*
- (void)viewDidUnload
{
    [self setMapView:nil];
    [super viewDidUnload];
    // Release any retained subviews of the main view.
}
*/
/*
- (BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation
{
    return (interfaceOrientation != UIInterfaceOrientationPortraitUpsideDown);
}
*/
@end
